from bs4 import BeautifulSoup;
from pytube import YouTube;
import os;
import sys;
import requests;

def downloadVideo(url , path):
    yt = YouTube(url);
    mp4files = yt.filter('mp4');
    print(yt.filename);
    print(mp4files[-1]);
    video = yt.get(mp4files[-1].extension , mp4files[-1].resolution);
    video.download(path);

url = input('Enter URL: ');
url = url.strip();
source_code = requests.get(url);
plain_text = source_code.text;
soup = BeautifulSoup(plain_text , 'html.parser');
save_path =  'N:/Videos/';
title = soup.find('h1' ,attrs={'class':'pl-header-title'}).text;
playlist_name = title.strip();
playlist_name = playlist_name.replace('|' , ' ');
playlist_name = playlist_name.replace('  ' , ' ');
save_path = save_path + playlist_name;
print(save_path);
os.mkdir(save_path);

for link in soup.find_all('a' , attrs={'class': 'pl-video-title-link'}) :
   downloadVideo('https://www.youtube.com/' + link.get('href') , save_path);
