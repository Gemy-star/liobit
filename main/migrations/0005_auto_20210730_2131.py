# Generated by Django 3.2.5 on 2021-07-30 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_categoryofbusiness_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryofbusiness',
            old_name='الأسم',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='categoryofbusiness',
            old_name='الوصف',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='contactrequests',
            old_name='البريد الألكترونى',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactrequests',
            old_name='الرسالة',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contactrequests',
            old_name='الأسم',
            new_name='personName',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='الأسم',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='اللينك',
            new_name='url',
        ),
    ]
