from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    """
    进入该聊天室
    """
    room = message['msg']
    join_room(room)
    session['room'] = room
    emit('status', {'msg': session.get('name') + ' 进入该聊天室'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """
    发送信息
    """
    print("room", session.get("room"))
    room = message.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """
    离开该聊天室
    """
    room = session.get('room')
    session.pop('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + '离开该聊天室'}, room=room)

