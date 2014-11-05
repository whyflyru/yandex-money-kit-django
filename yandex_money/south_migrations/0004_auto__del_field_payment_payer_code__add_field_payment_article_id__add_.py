# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Payment', fields ['customer_number']
        db.delete_unique(u'yandex_money_payment', ['customer_number'])

        # Deleting field 'Payment.payer_code'
        db.delete_column(u'yandex_money_payment', 'payer_code')

        # Adding field 'Payment.article_id'
        db.add_column(u'yandex_money_payment', 'article_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Payment.order_number'
        db.add_column(u'yandex_money_payment', 'order_number',
                      self.gf('django.db.models.fields.CharField')(max_length=64, unique=True, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Payment.order_amount'
        db.alter_column(u'yandex_money_payment', 'order_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2))

        # Changing field 'Payment.cps_email'
        db.alter_column(u'yandex_money_payment', 'cps_email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True))

    def backwards(self, orm):
        # Adding field 'Payment.payer_code'
        db.add_column(u'yandex_money_payment', 'payer_code',
                      self.gf('django.db.models.fields.CharField')(max_length=33, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Payment.article_id'
        db.delete_column(u'yandex_money_payment', 'article_id')

        # Deleting field 'Payment.order_number'
        db.delete_column(u'yandex_money_payment', 'order_number')


        # Changing field 'Payment.order_amount'
        db.alter_column(u'yandex_money_payment', 'order_amount', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Payment.cps_email'
        db.alter_column(u'yandex_money_payment', 'cps_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))
        # Adding unique constraint on 'Payment', fields ['customer_number']
        db.create_unique(u'yandex_money_payment', ['customer_number'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'yandex_money.payment': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Payment'},
            'article_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cps_email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cps_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'customer_number': ('django.db.models.fields.CharField', [], {'default': "'e52ba3530c864d96a76987e2b09263a7'", 'max_length': '64'}),
            'fail_url': ('django.db.models.fields.URLField', [], {'default': "'http://example.com/fail-payment/'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'order_currency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '643'}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'pc'", 'max_length': '2'}),
            'performed_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'scid': ('django.db.models.fields.PositiveIntegerField', [], {'default': '123'}),
            'shop_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'shop_currency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '643', 'null': 'True', 'blank': 'True'}),
            'shop_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '456'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'processed'", 'max_length': '16'}),
            'success_url': ('django.db.models.fields.URLField', [], {'default': "'http://example.com/success-payment/'", 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['yandex_money']