from django.db import models
import uuid

class Group(models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Title', max_length=128)
    photo = models.TextField('Photo', blank=True, null=True)
    description = models.TextField('Description', null=True, blank=True)
    idAdmin = models.ForeignKey('user.user', on_delete=models.PROTECT)
    isTransmission = models.BooleanField('Transmission', default=False)
    isPrivate = models.BooleanField('Private', default=True)
    archive = models.BooleanField('Archived', default=False)

    participants = models.ManyToManyField(
        'user.user',
        verbose_name='participants',
        related_name='participants',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Groups"

class Message(models.Model):
    PRIORITY = (
        (0, 'Normal'),
        (1, 'Urgent'),
    )

    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField('Message')
    date = models.DateTimeField('Sent date', auto_now_add=True)
    priority = models.IntegerField('Priority', choices=PRIORITY, default=0)
    idSentBy = models.ForeignKey('user.user', on_delete=models.PROTECT)
    idGroup = models.ForeignKey('group.group', on_delete=models.PROTECT)

    pkeSentBy = models.CharField('pke', max_length=128, blank=True, null=True)
    pkeReceiver = models.CharField('pke', max_length=128, blank=True, null=True)#this is not going to work for group chats.

    readBy = models.ManyToManyField(
        'user.user',
        verbose_name='Read By',
        related_name='readBy',
        blank=True,
    )
    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['date']
        verbose_name_plural = "Messages"
