import requests

def findEnd(endseq, rem, remlen):
  curr_btn = ""; num = 0
  end = rem[num-len(endseq):num]
  while(end != endseq and num<=remlen):
    curr_btn += rem[num]
    num+=1
    end = rem[num:num+len(endseq)]
  curr_btn += rem[num:num+len(endseq)]
  return curr_btn

def find_tags_OC(inpt, id): # find tags that open and close ie <a></a> and <button></button>
  buttons = list(""); i=0
  for c in inpt:
    if (inpt[i:i+len(id)] == id): # inpt[i] = <
      buttons.append(findEnd("</"+inpt[i+1:i+len(id)]+">",inpt[i:],len(inpt[i:])))
    i+=1
  return buttons

def find_tags_ONC(inpt, id): # find tags that open but don't close- ie <input>
  buttons = list(""); i=0
  for c in inpt:
    if (inpt[i:i+len(id)] == id): # inpt[i] = <
      buttons.append(findEnd(">",inpt[i:],len(inpt[i:])))
    i+=1
  return buttons

def find_imgbtns(buttons):
  img_btns = list("")
  for s in buttons:
    i=0
    for c in s:
      if (i+3 < len(s)):
        if (s[i:i+3]=="svg" or s[i:i+3]=="img" or s[i:i+4]=="src=" or s[i:i+4]=="src ="): # searching for svg or img src 
          img_btns.append(s)
        i=i+1
  return img_btns


def extract_img_link(img_btns):
  sources = list(""); s = 0
  for b in img_btns:
    i=0; start = False; source = ""
    while (i<len(b)):
      if (b[i:i+4]=="src="):
        start=True
        i=i+5
      if (start):
        if (b[i]=='"'):
          start=False
        else:
          source+=b[i]
      i=i+1
    sources.append(source)
  return sources
def extract_FFL(img_link): # extract final from link
  # find the last slash
  i = 0; last_slash = -1; dot = -1
  for c in img_link:
    if (c == '/'):
      last_slash = i
    if (c == '.'):
      dot = i
    i+=1
  return (img_link[last_slash+1:dot])

def main(html):
    
    #r = requests.get(url)
    data = html
    
    buttons = find_tags_OC(data, "<a")
    buttons += find_tags_OC(data, "<button")
    buttons += find_tags_ONC(data, "<input")
     
    img_btns = find_imgbtns(buttons)

    print(img_btns)
    
    #final_extr = list("")
    img_links = list("")
    for b in extract_img_link(img_btns):
      print(b)
      img_links.append(b)
      #final_extr.append(extract_FFL(b))
    
    return(img_links)
