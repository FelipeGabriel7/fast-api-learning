from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='Felipe Gabriel',
        password='secret',
        email='Felipe1@example.com',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(User).where(User.username == 'Felipe Gabriel')
    )

    assert user.username == 'alice'
