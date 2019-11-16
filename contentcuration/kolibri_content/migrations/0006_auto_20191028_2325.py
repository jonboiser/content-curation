# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-28 23:25
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20190424_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='extension',
            field=models.CharField(blank=True, choices=[(b'mp4', b'MP4 Video'), (b'vtt', b'VTT Subtitle'), (b'mp3', b'MP3 Audio'), (b'pdf', b'PDF Document'), (b'jpg', b'JPG Image'), (b'jpeg', b'JPEG Image'), (b'png', b'PNG Image'), (b'gif', b'GIF Image'), (b'json', b'JSON'), (b'svg', b'SVG Image'), (b'perseus', b'Perseus Exercise'), (b'graphie', b'Graphie Exercise'), (b'zip', b'HTML5 Zip'), (b'h5p', b'H5P'), (b'epub', b'ePub Document')], max_length=40),
        ),
        migrations.AlterField(
            model_name='file',
            name='preset',
            field=models.CharField(blank=True, choices=[(b'high_res_video', b'High Resolution'), (b'low_res_video', b'Low Resolution'), (b'video_thumbnail', b'Thumbnail'), (b'video_subtitle', b'Subtitle'), (b'video_dependency', b'Video (dependency)'), (b'audio', b'Audio'), (b'audio_thumbnail', b'Thumbnail'), (b'document', b'Document'), (b'epub', b'ePub Document'), (b'document_thumbnail', b'Thumbnail'), (b'exercise', b'Exercise'), (b'exercise_thumbnail', b'Thumbnail'), (b'exercise_image', b'Exercise Image'), (b'exercise_graphie', b'Exercise Graphie'), (b'channel_thumbnail', b'Channel Thumbnail'), (b'topic_thumbnail', b'Thumbnail'), (b'html5_zip', b'HTML5 Zip'), (b'html5_dependency', b'HTML5 Dependency (Zip format)'), (b'html5_thumbnail', b'HTML5 Thumbnail'), (b'h5p', b'H5P Zip'), (b'slideshow_image', b'Slideshow Image'), (b'slideshow_thumbnail', b'Slideshow Thumbnail'), (b'slideshow_manifest', b'Slideshow Manifest')], max_length=150),
        ),
        migrations.AlterField(
            model_name='localfile',
            name='extension',
            field=models.CharField(blank=True, choices=[(b'mp4', b'MP4 Video'), (b'vtt', b'VTT Subtitle'), (b'mp3', b'MP3 Audio'), (b'pdf', b'PDF Document'), (b'jpg', b'JPG Image'), (b'jpeg', b'JPEG Image'), (b'png', b'PNG Image'), (b'gif', b'GIF Image'), (b'json', b'JSON'), (b'svg', b'SVG Image'), (b'perseus', b'Perseus Exercise'), (b'graphie', b'Graphie Exercise'), (b'zip', b'HTML5 Zip'), (b'h5p', b'H5P'), (b'epub', b'ePub Document')], max_length=40),
        ),
    ]