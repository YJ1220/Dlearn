#-*-coding: utf-8-*-
from django.db import models
from DjangoUeditor.models import UEditorField
# 生成相关的网址
from django.core.urlresolvers import reverse

# Create your models here.
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)




    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']

class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=250, unique=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')

# 修改编辑框信息
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')

    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=(self.slug,))

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
# Create your models here.
