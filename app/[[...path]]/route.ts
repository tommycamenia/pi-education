import shell from '../shell';
import mobileShell from '../shell-mobile';
import mobileOriginals from '../original-mobile-routes.json';
import originals from '../original-routes.json';
import { env } from 'cloudflare:workers';
export async function GET(request:Request){const url=new URL(request.url),path=url.pathname.replace(/\/$/,'')||'/';const mobile=/Mobile|Android|iPhone|iPad/i.test(request.headers.get('user-agent')||'')||url.searchParams.get('view')==='mobile';const asset=((mobile?mobileOriginals:originals) as Record<string,string>)[path]||(originals as Record<string,string>)[path];if(asset&&!['/form-coba-gratis','/dokumen-pendaftaran-siswa-baru','/forum','/live-video'].includes(path)){const bindings=env as unknown as {ASSETS:{fetch(request:Request):Promise<Response>}};const u=new URL(asset,url);const r=await (import.meta.env.DEV?fetch(u):bindings.ASSETS.fetch(new Request(u,{method:'GET'})));return new Response(r.body,{status:r.status,headers:{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-cache'}})}return new Response(mobile?mobileShell:shell,{headers:{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-cache'}})}
