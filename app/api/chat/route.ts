import {runtime,json,identity,admin,writeAllowed} from '../common';
export async function GET(req:Request){
 const u=identity(req);if(!u.id)return json({error:'Masuk untuk membuka percakapan pribadi.'},401);
 const url=new URL(req.url),all=url.searchParams.get('admin')==='1',owner=url.searchParams.get('owner')||u.id;
 if((all||owner!==u.id)&&!admin(req))return json({error:'Percakapan tidak ditemukan.'},403);
 const db=runtime().DB;
 if(all){const rows=await db.prepare('SELECT owner,name,email,MAX(created_at) AS updated_at FROM chat_messages WHERE role=? GROUP BY owner ORDER BY updated_at DESC LIMIT 200').bind('parent').all();return json({threads:rows.results})}
 const rows=await db.prepare('SELECT id,role,body,created_at FROM (SELECT id,role,body,created_at FROM chat_messages WHERE owner=? ORDER BY created_at DESC,id DESC LIMIT 200) ORDER BY created_at,id').bind(owner).all();return json({messages:rows.results,email:u.email,isAdmin:admin(req)})
}
export async function POST(req:Request){
 const u=identity(req);if(!u.id)return json({error:'Masuk untuk mengirim pesan.'},401);if(!writeAllowed(req))return json({error:'Permintaan tidak diizinkan.'},403);
 const raw=await req.text();if(raw.length>8000)return json({error:'Pesan terlalu panjang.'},413);let b;try{b=JSON.parse(raw)}catch{return json({error:'Data tidak valid.'},400)}
 if(!b||typeof b!=='object'||Array.isArray(b))return json({error:'Data tidak valid.'},400);
 const body=typeof b.body==='string'?b.body.trim():'';if(!body||body.length>2000||!/^[-a-zA-Z0-9]{16,80}$/.test(b.request_key||''))return json({error:'Isi pesan maksimal 2000 karakter.'},400);
 const replying=b.owner!==undefined;if(replying&&!admin(req))return json({error:'Akses ditolak.'},403);const owner=replying?b.owner:u.id;if(typeof owner!=='string'||!owner||owner.length>200)return json({error:'Percakapan tidak valid.'},400);
 const db=runtime().DB;if(replying&&!await db.prepare('SELECT id FROM chat_messages WHERE owner=? LIMIT 1').bind(owner).first())return json({error:'Percakapan tidak ditemukan.'},404);
 const name=typeof b.name==='string'?b.name.trim():'',phone=typeof b.phone==='string'?b.phone.trim():'';
 if(!replying&&(!name||name.length>100||!/^[+\d ()-]{8,25}$/.test(phone)))return json({error:'Lengkapi nama dan nomor telepon.'},400);
 const prior=await db.prepare('SELECT id FROM chat_messages WHERE owner=? AND request_key=?').bind(owner,b.request_key).first();if(prior)return json({message:prior});
 const count=await db.prepare('SELECT COUNT(*) AS n FROM chat_messages WHERE owner=? AND role=? AND created_at>?').bind(owner,replying?'school':'parent',new Date(Date.now()-3600000).toISOString()).first<{n:number}>();if((count?.n||0)>=60)return json({error:'Batas pesan tercapai. Silakan coba lagi nanti.'},429);
 const id=crypto.randomUUID();await db.prepare('INSERT INTO chat_messages (id,owner,request_key,role,name,email,phone,body,created_at) VALUES (?,?,?,?,?,?,?,?,?)').bind(id,owner,b.request_key,replying?'school':'parent',replying?'Pengelola sekolah':name,u.email,phone,body,new Date().toISOString()).run();return json({message:{id}},201)
}
