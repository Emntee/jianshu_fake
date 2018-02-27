# coding = utf-8
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

import os

# Create your models here
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('头像', upload_to='uploads/thumbnail/avatar')
    mobile = models.CharField('手机号', max_length=14, blank=True, null=True)


# 文章相关的model，包括article, comment, in-article image
class Article(models.Model):
    class meta:
        ordering = ['publish_time',]
    CONTENT_TYPES= (
        ('md', 'markdown file'),
        ('rt', 'richtext file'),
    )
    title = models.CharField('标题', max_length=settings.ARTICLE_MAX_TITLE_LENGTH)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    
    content = models.TextField('原始内容')
    content_type = models.CharField('内容类型', max_length=4, choices=CONTENT_TYPES)
    abstract = models.TextField('摘要')
    img_view = models.ImageField('缩略图', upload_to='uploads/thumbnail/article')
    _tags = models.TextField('标签')

    edit_time = models.DateTimeField('上次改动时间', auto_now=True)
    publish_time = models.DateTimeField('发布时间', blank=True, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    voted_up = models.IntegerField('支持', default=0)
    voted_down = models.IntegerField('反对', default=0)
    viewed = models.IntegerField('浏览', default=0)

    @property
    def heat(self):
        """通过算法计算热度并返回"""
        pass

    @property
    def all_comments(self):
        return self.comments.all()

    @property
    def commented(self):
        return len(self.all_comments)

    @property
    def tags(self):
        return self._tags.split('#')

    def add_tag(self, new_tag):
        self._tags = self._tags + '#' + new_tag
        self.save()

    def has_img(self):
        return self.img_view

    def __str__(self):
        return '{} (by {} at {})'.format(self.title, self.author.username, self.create_time.strftime("%Y%m%d_%H%M%S"))


class InArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/image/article')

    def __str__(self):
        return os.path.basename(self.image.name)


class Comment(models.Model):
    class meta: 
        ordering = ['create_time',]
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    create_time = models.DateTimeField('发表时间', auto_now_add=True)
    content = models.TextField('评论内容')
   

# 主页轮播内容
class CarouselSlide(models.Model):
    class meta:
        ordering = ['create_time',]
    title = models.CharField('banner标题', max_length=25)
    img = models.ImageField('图片', upload_to='uploads/image/slides')
    description = models.CharField('banner描述', max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)


# 兴趣组
class Collection(models.Model):
    class meta:
        ordering = ['heat']
    
    creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    admin = models.ManyToManyField(User, related_name='collections_in_charge')
    members = models.ManyToManyField(User, related_name='collections')
    name = models.CharField('兴趣组名称', max_length=14)
    info = models.TextField('兴趣组说明')

    thumbnail = models.ImageField('缩略图', upload_to='uploads/thumbnail/collections')

    def __str__(self):
        return self.name
