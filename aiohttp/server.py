from aiohttp import web

async def hello(request):
    text = """  


    hhhhhhh                                lllllll lllllll                  
    h:::::h                                l:::::l l:::::l                  
    h:::::h                                l:::::l l:::::l                  
    h:::::h                                l:::::l l:::::l                  
    h::::h hhhhh           eeeeeeeeeeee    l::::l  l::::l    ooooooooooo   
    h::::hh:::::hhh      ee::::::::::::ee  l::::l  l::::l  oo:::::::::::oo 
    h::::::::::::::hh   e::::::eeeee:::::eel::::l  l::::l o:::::::::::::::o
    h:::::::hhh::::::h e::::::e     e:::::el::::l  l::::l o:::::ooooo:::::o
    h::::::h   h::::::he:::::::eeeee::::::el::::l  l::::l o::::o     o::::o
    h:::::h     h:::::he:::::::::::::::::e l::::l  l::::l o::::o     o::::o
    h:::::h     h:::::he::::::eeeeeeeeeee  l::::l  l::::l o::::o     o::::o
    h:::::h     h:::::he:::::::e           l::::l  l::::l o::::o     o::::o
    h:::::h     h:::::he::::::::e         l::::::ll::::::lo:::::ooooo:::::o
    h:::::h     h:::::h e::::::::eeeeeeee l::::::ll::::::lo:::::::::::::::o
    h:::::h     h:::::h  ee:::::::::::::e l::::::ll::::::l oo:::::::::::oo 
    hhhhhhh     hhhhhhh    eeeeeeeeeeeeee llllllllllllllll   ooooooooooo   
    """
    print('received request, saying hello')
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/hello', hello)

web.run_app(app, port=8888)