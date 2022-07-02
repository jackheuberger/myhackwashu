# Generated by Django 3.2.7 on 2022-06-29 02:46

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0039_sponsorapplication_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackerapplication',
            name='graduation_year',
            field=models.IntegerField(choices=[(2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')], default=2023),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='graduation_year',
            field=models.IntegerField(choices=[(2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')], default=2023),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='which_hack',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'HackWashU 2016 Fall'), (1, 'HackWashU 2016 Winter'), (2, 'HackWashU 2017 Fall'), (3, 'HackWashU 2017 Winter'), (4, 'HackWashU 2018'), (5, 'HackWashU 2019'), (6, 'HackWashU2021')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='graduation_year',
            field=models.IntegerField(choices=[(2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')], default=2023),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='which_hack',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'HackWashU 2016 Fall'), (1, 'HackWashU 2016 Winter'), (2, 'HackWashU 2017 Fall'), (3, 'HackWashU 2017 Winter'), (4, 'HackWashU 2018'), (5, 'HackWashU 2019'), (6, 'HackWashU2021')], max_length=13, null=True),
        ),
    ]
