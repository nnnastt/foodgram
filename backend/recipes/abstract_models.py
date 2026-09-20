from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseUserRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        'recipes.Recipe',
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        abstract = True
        default_related_name = '%(class)ss'

    def __str__(self):
        return f'{self.user} -> {self.recipe}'
