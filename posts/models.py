from django.db import models


# model class
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


#  gallery model
class PostImage(models.Model):
    post = models.ForeignKey(Post,
                             default=None,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title
