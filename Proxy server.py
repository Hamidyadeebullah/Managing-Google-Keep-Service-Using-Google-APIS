from flask import Flask, jsonify, request
import gkeepapi

app = Flask(__name__)

keep = gkeepapi.Keep()
keep.login("hamidy.adeebullah@gmail.com", 'hmrj ooxq ewyf riqj')

@app.route('/create_note', methods=['POST'])
def create_note():
    title = request.json.get('title')
    text = request.json.get('text')
    gnote = keep.createNote(title, text)
    keep.sync()
    return jsonify({'note_id': gnote.id})

@app.route('/show_all_notes', methods=['GET'])
def show_all_notes():
    notes = keep.all()
    all_notes = []

    for note in notes:
        text = note.text.replace("☐ ", "").replace("☑ ", "").replace("Item 2","")
        all_notes.append({"id": note.id, "title": note.title, "text": text})

    return jsonify(all_notes)

@app.route('/delete_note/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = keep.get(note_id)
    if note:
        note.delete()
        keep.sync()
        return jsonify({'message': 'Note deleted successfully.'})
    else:
        return jsonify({'error': 'Note not found.'})
@app.route('/modify_note/<note_id>', methods=['PUT'])
def modify_note(note_id):
    note = keep.get(note_id)
    if note:
        title = request.json.get('title')
        text = request.json.get('text')
        note.title = title
        note.text = text
        keep.sync()
        return jsonify({'message': 'Note modified successfully.'})
    else:
        return jsonify({'error': 'Note not found.'})
    
if __name__ == '__main__':
    app.run(debug=True)
