def generate_bc(url, separator):
    url_list=url.split("/")
    for i in range(0,len(url_list)):
        if i==0:
            url_list[i]='<a href="/">HOME</a>'
        elif i==len(url_list)-1:
            url_list[i]=f'<span class="active">{(url_list[i].split(".")[0]).upper()}</span>'
        else:
            url_list[i]=f'<a href="/{url_list[i]}/">{url_list[i].upper()}</a>'
    
    return separator.join(url_list)


url= "mysite.com/pictures/holidays.html"
separator= " : "
print(
    generate_bc(url,separator)
)