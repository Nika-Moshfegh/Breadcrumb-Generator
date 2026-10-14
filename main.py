def find_symbol(url):
    symbol=["?",".","/","#"]
    for i in symbol:
        fs=url.find(i)
        if fs!=-1:
            url=url[:fs]
            
    return url
        
def Abbreviation(url):
    res=""
    if len(url)<30:
        return url
    
    url_list=url.split("-")
    for i in url_list:
        if i not in ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]:
            res+=i[0].upper()
    return res
            
        
def generate_bc(url, separator):

    url_list=url.split("/")
    for i in range(0,len(url_list)):
        if i==0:
            url_list[i]='<a href="/">HOME</a>'
        elif i==len(url_list)-1:
            url_list[i]=find_symbol(url_list[i])
            url_list[i]=Abbreviation(url_list[i])
            url_list[i]=f'<span class="active">{(url_list[i]).upper()}</span>'
        else:
            url_list[i]=Abbreviation(url_list[i])
            url_list[i]=f'<a href="/{url_list[i]}/">{url_list[i].upper()}</a>'
    
    return separator.join(url_list)


url= "mysite.com/pictures/holidays.html"
separator= " : "
print(
    generate_bc(url,separator)
)

