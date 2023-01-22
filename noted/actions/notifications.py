from typing import Union, List

from notifications.signals import notify

from django.utils.functional import SimpleLazyObject

from actions.base import CREATE, FOLLOW, LIKE
from content.models import Note
from tags.models import get_tag_followers, UnicodeTag
from users.models import User, Following


RECIPIENTS_GETTERS = {
    (User, FOLLOW, User): lambda _, followed_user: followed_user,
    (User, LIKE, Note): lambda _, note: note.author,
    # TODO: Exclude AUTHOR of Tag
    (UnicodeTag, CREATE, Note): lambda tag, _: get_tag_followers(tag),
    (User, CREATE, Note): lambda author, _: Following.objects.get_follower(
        author
    ),
}


def get_recipients(actor, verb: str, target) -> Union[User, List[User], None]:
    """Retrieves the recipients of an action based on the actor, verb and target.

    This function takes in three arguments: `actor`, `verb`, and `target`.
    The `actor` and `target` arguments are instances of an object, whereas
    the `verb` argument is a string representing the action taken by the `actor`.

    It returns None if the recipient function is not found.

    Args:
        actor (Object): an instance of an object representing the actor of
                        the action.
        verb (str): a string representing the verb of the action
        target (Object): an instance of an object representing the target of
                        the action.

    Returns:
        The recipients of the given action. It can be single user or a list
        of users. It returns None if the recipient function is not found.
    """
    actor_type = User if isinstance(actor, SimpleLazyObject) else type(actor)
    targ_type = User if isinstance(target, SimpleLazyObject) else type(target)
    recipient_function = RECIPIENTS_GETTERS.get((actor_type, verb, targ_type))
    return recipient_function(actor, target) if recipient_function else None


def create_notification(actor, verb: str, target):
    """Creates a notification based on the actor, verb, and target of an action.

    Args:
        actor (Object): an instance of an object representing the actor of
                        the action.
        verb (str): a string representing the verb of the action.
        target (Object): an instance of an object representing the target of
                         the action.
    """
    notify.send(
        actor,
        verb=verb,
        recipient=get_recipients(actor, verb, target),
        target=target,
    )
