# Jalankan: python build.py  ->  dist/ichaa-squad.html (satu file, gambar tertanam)
import re,base64,pathlib
r=pathlib.Path(__file__).parent;h=(r/'index.html').read_text()
M={'webp':'image/webp','png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg'}
def inl(m):
    f=r/'assets/characters'/m.group(2)
    return m.group(1)+"'data:%s;base64,%s'"%(M[f.suffix[1:].lower()],base64.b64encode(f.read_bytes()).decode())
h=re.sub(r"(\b(?:levi|eren|nouzen|mikasa|akame|lena):)'([^']+\.(?:webp|png|jpe?g))'",inl,h)
h=h.replace("const ASSET='assets/characters/';","const ASSET='';")
(r/'dist').mkdir(exist_ok=True);(r/'dist'/'ichaa-squad.html').write_text(h);print('OK dist/ichaa-squad.html')
