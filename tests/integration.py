"""Local-only API integration checks. Uses synthetic records; never run against production."""
import urllib.request,urllib.error,json,uuid,datetime,base64
BASE='http://127.0.0.1:5174';owner='test-'+str(uuid.uuid4());checks=0

def call(path,method='GET',body=None,user=owner,email='test@example.test',origin=BASE,raw=None,content=None):
 headers={}
 if user:headers.update({'oai-authenticated-user-id':user,'oai-authenticated-user-email':email})
 if method!='GET':headers['Origin']=origin
 if body is not None:raw=json.dumps(body).encode();headers['Content-Type']='application/json'
 if content:headers['Content-Type']=content
 req=urllib.request.Request(BASE+path,data=raw,headers=headers,method=method)
 try:r=urllib.request.urlopen(req);return r.status,r.read()
 except urllib.error.HTTPError as e:return e.code,e.read()
def expect(code,result):
 global checks
 assert result[0]==code,(code,result);checks+=1
 return json.loads(result[1]) if result[1].startswith(b'{') else result[1]
expect(401,call('/api/requests',user=None));expect(403,call('/api/requests?admin=1'))
key=str(uuid.uuid4());base=dict(kind='trial',request_key=key,guardian='TEST GUARDIAN',email='test@example.test',phone='080000000000',child='TEST PARTICIPANT',dob='2020-01-01',program='Homeschooling SD',campus='Colombo',preferred_date='',preferred_time='',notes='Synthetic local integration test',consent='yes')
expect(403,call('/api/requests','POST',base,origin='https://other.example'))
expect(400,call('/api/requests','POST',{**base,'consent':'no'}))
first=expect(201,call('/api/requests','POST',base))['request'];again=expect(200,call('/api/requests','POST',base))['request'];assert first['id']==again['id']
expect(400,call('/api/requests','POST',{**base,'kind':'booking','request_key':str(uuid.uuid4())}))
for kind in ['enrollment','booking']:
 b={**base,'kind':kind,'request_key':str(uuid.uuid4()),'preferred_date':(datetime.date.today()+datetime.timedelta(days=30)).isoformat()};expect(201,call('/api/requests','POST',b))
rows=expect(200,call('/api/requests'))['requests'];assert len(rows)==3
assert expect(200,call('/api/requests',user='other-test'))['requests']==[]
id=first['id'];patch=dict(id=id,status='confirmed',version=1)
expect(403,call('/api/requests','PATCH',patch));expect(404,call('/api/requests','PATCH',{**patch,'status':'cancelled'},user='other-test'))
expect(200,call('/api/requests','PATCH',patch,user='local_seedy',email='seedy@sites.test'))
expect(409,call('/api/requests','PATCH',patch,user='local_seedy',email='seedy@sites.test'))
assert next(r for r in expect(200,call('/api/requests'))['requests'] if r['id']==id)['status']=='confirmed'
blob=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII=');boundary='TEST'+uuid.uuid4().hex
multipart=(f'--{boundary}\r\nContent-Disposition: form-data; name="request"\r\n\r\n{id}\r\n--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="test.png"\r\nContent-Type: image/png\r\n\r\n'.encode()+blob+f'\r\n--{boundary}--\r\n'.encode())
expect(403,call('/api/files','POST',user='other-test',raw=multipart,content='multipart/form-data; boundary='+boundary))
f=expect(201,call('/api/files','POST',raw=multipart,content='multipart/form-data; boundary='+boundary))['file'];expect(403,call('/api/files?request='+id,user='other-test'));files=expect(200,call('/api/files?request='+id))['files'];assert len(files)==1
received=expect(200,call('/api/files?request='+id+'&file='+f['id']));assert received==blob
expect(403,call('/api/files?request='+id+'&file='+f['id'],user='other-test'))
print('Passed',checks,'API checks: persistence, idempotency, registration, booking, permissions, status conflicts, document storage and download.')
