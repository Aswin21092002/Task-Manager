# Generated by Django 3.2.6 on 2023-11-26 18:15

from django.db import migrations
from django.conf import settings
import stripe


def forwards_func(apps, schema_editor):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        product = stripe.Product.create(name="Business Credit Report")
        price = stripe.Price.create(unit_amount=3999, currency="usd", product=product['id'],
                                    recurring=None)
        Plan = apps.get_model("bankapp", "Plan")
        Plan.objects.create(plan_name='Buy Business Report', stripe_id=price['id'], price=3999)
    except Exception as e:
        print(e)


def reverse_func(apps, schema_editor):
    Plan = apps.get_model("bankapp", "Plan")
    Plan.objects.filter(plan_name='Buy Business Report', price=3999).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_stripecustomer'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
