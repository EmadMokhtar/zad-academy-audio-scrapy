import asyncio
import os
import httpx
from mutagen.easyid3 import EasyID3

audio_file_path_template = ('https://resources.zad-academy.com/Semester'
                            '{semester}/{course}/Audios/')
file_name_template = 'Lecture{lecture}_{course}_Semester{semester}.mp3'
zad_courses = ['Aqeedah', 'Tafsir', 'Hadith', 'Seerah', 'Arabic', 'Tarbiyah',
               'Fiqh']

downloaded_already = []


async def download_semester(semester, output_dir):
    """
    Function to download ZAD Academy's audio lectures based on a semester.
    :param semester: Semester number
    :param output_dir: Directory path where Audio files will be saved.
    :return: None
    """
    for course in zad_courses:
        for i in range(1, 25):
            file_name = file_name_template.format(lecture=i,
                                                  semester=semester,
                                                  course=course)
            file_url = os.path.join(
                audio_file_path_template.format(course=course,
                                                semester=semester),
                file_name
            )
            # TODO: Check for the file before downloading it.
            print(f'Downloading {file_name}')
            async with httpx.AsyncClient() as client:
                file_request_response = await client.get(file_url)
                if file_request_response.status_code == httpx.codes.OK:
                    with open(os.path.join(output_dir, file_name), 'wb') as f:
                        f.write(file_request_response.content)
                        album, *album = file_name.split('_')
                        mp3file = EasyID3(os.path.join(output_dir, file_name))
                        mp3file['album'] = album
                        mp3file['artist'] = 'ZAD Academy'
                        mp3file['title'] = file_name.split('.')[0]
                        mp3file['tracknumber'] = f'0{i}'
                        mp3file.save()
                        # TODO: Log the successful downloaded file in order not to download it again
                        print(f'Saved {file_name}')
                else:
                    print(f'Something happened can not download {file_name}')


if __name__ == '__main__':
    asyncio.run(download_semester(2, './audio'))
