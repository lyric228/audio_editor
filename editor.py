from pydub import AudioSegment


def edit_audio(sound_start: int, sound_end: int, filename: str, extension: str):
    audio = AudioSegment.from_mp3(f"static/sounds/15 06/{filename}.{extension}")
    audio = audio[sound_start:sound_end]
    audio.export(f"static/sounds/15 06/edited/{filename}.{extension}", format=extension)
