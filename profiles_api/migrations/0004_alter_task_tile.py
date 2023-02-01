

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.tile'),
        ),
    ]
