#配置环境
##主要配置环境
    Python:    3.6
    Django:    1.8.3
##其他环境：
###DjangoUeditor：服务文本编辑器
下载地址：
https://github.com/twz915/DjangoUeditor3/archive/master.zip
    
    下载 DjangoUeditor ，解压。将内部文件 DjangoUeditor-master复制到APP同级目录
    1.在settings.py 中加入  DjangoUeditor 这个应用
    `INSTALLED_APPS = (
        ...
       
        'DjangoUeditor',
    )`   
    ****
    2.在 urls.py 中添加一行：
    from DjangoUeditor import urls as DjangoUeditor_urls
 
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^ueditor/', include(DjangoUeditor_urls)),
     ]
    ****
    3.为了让上传的图片，文件可以在本地调试的时候可以正常显示，下载，在settings.py 设置 static 和 media

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
     
    # 公共的 static 文件，比如 jquery.js 可以放这里，这里面的文件夹不能包含 STATIC_ROOT
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "common_static"),
    )
     
    # upload folder
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
    
    在urls.py 最后加入以下代码：
    # use Django server /media/ files
    from django.conf import settings
     
    if settings.DEBUG:
        from django.conf.urls.static import static
        urlpatterns += static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
###pymysql:Django默认支持MySQLdb
    在站点的 __init__.py 文件中添加
	import pymysql
	pymysql.install_as_MySQLdb()

    
    
 
 