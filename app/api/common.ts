import { env } from 'cloudflare:workers';
export const runtime = () => env as unknown as {DB:D1Database;BUCKET:R2Bucket;ADMIN_EMAIL:string};
export const json=(data:unknown,status=200)=>Response.json(data,{status,headers:{'Cache-Control':'no-store'}});
export function identity(req:Request){return {id:req.headers.get('oai-authenticated-user-id')||'',email:req.headers.get('oai-authenticated-user-email')||''}}
export function admin(req:Request){const e=runtime();return !!e.ADMIN_EMAIL && identity(req).email.toLowerCase()===e.ADMIN_EMAIL.toLowerCase()}
export function writeAllowed(req:Request){const origin=req.headers.get('origin');return origin===new URL(req.url).origin && req.headers.get('sec-fetch-site')!=='cross-site'}
export async function owns(req:Request,id:string){const u=identity(req);if(!u.id)return null;const row=await runtime().DB.prepare('SELECT * FROM requests WHERE id=?').bind(id).first();return row&&(row.owner===u.id||admin(req))?row:null}
