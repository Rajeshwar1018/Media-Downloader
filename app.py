from flask import Flask,render_template,request,redirect
import youtube_dl
import re


app = Flask(__name__)


@app.route('/twitter')
def twitter():
	return render_template('twitter.html')

@app.route('/insta')
def insta():
	return render_template('insta.html')

@app.route('/yt')
def yt():
	return render_template('yt.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=["POST","GET"])
def download():
	url = request.form["url"]
	print("Someone just tried to download", url)
	return new_func(url)

def new_func(url):
    try:        
             with youtube_dl.YoutubeDL() as ydl:
               url = ydl.extract_info(url, download=False)
               print(url)
               try:
                  download_link = url["entries"][-1]["formats"][-1]["url"]
               except:
                  download_link = url["formats"][-1]["url"]
               print(download_link)
               return redirect(download_link + "&dl=1")
    except:
         return render_template('error4.html')
         pass

@app.route('/download1', methods=["POST","GET"])		
def download1():      
     url = request.form["url"]
     print("Someone just tried to download", url)
     regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
     print(url)
     if not re.match(regex,url):
            print('nhi hoa')
            response = "Enter Youtube Url"
            return render_template('error.html')
     try:        
      with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(url, download=False)
        print(url)
        video_streams = []
        for i in url['formats']:
            file_size = i['filesize']
            print(file_size)
            if file_size is not None:
                file_size = f'{round(int(file_size) / 1000000,2)} mb'
                print(file_size)

            resolution = 'Audio'
            if i['height'] is not None:
                resolution = f"{i['height']}x{i['width']}"
                print(resolution)
            video_streams.append({
                'resolution': resolution,
                'extension': i['ext'],
                'file_size': file_size,
                'url': i['url']
            })
        print(type(video_streams))    
        video_streams = video_streams[::-1]
        
        context = {
            
            'title': url['title'], 'streams': video_streams,
            'description': url['description'], 'likes': url['like_count'],
            'dislikes': url['dislike_count'], 'thumb': url['thumbnails'][3]['url'],
            'duration': round(int(url['duration'])/60, 2), 'views': f'{int(url["view_count"]):,}'
        }
        print(context["thumb"])
        

        try:
            download_link = url["entries"][-1]["formats"][-1]["url"]
        except:
            download_link = url["formats"][-1]["url"]
        print(download_link)     
        return render_template('ytpage.html', context=context , streams = video_streams)
     except:
        return render_template('error.html')
        pass     


@app.route('/download2', methods=["POST","GET"])
def download2():
    url = request.form["url"]
    print("Someone just tried to download", url)
    try: 
     with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(url, download=False)
        #print(url) #it will print all streams once
        video_streams = []
        for i in url['formats']:
            
            print(i['url'])  #it will print url of each stream 
            resolution = 'Audio'
            if i['height'] is not None:
                resolution = f"{i['height']}x{i['width']}"
                print(resolution) #it will print resolution of each stream
            video_streams.append({
                'resolution': resolution,
                'extension': i['ext'],
                'url': i['url']
            })
        print(type(video_streams))    
        video_streams = video_streams[::-1]
        
        context = {
            
            'title': url['title'], 'streams': video_streams,
            'description': url['description'], 'likes': url['like_count'],
            'thumb': url['thumbnail']
            
        }
        print(context['likes'])
        print(context['thumb'])
        try:
            download_link = url["entries"][-1]["formats"][-1]["url"]
        except:
            download_link = url["formats"][-1]["url"]
        print(download_link) 
        return render_template('instapage.html', context=context , streams = video_streams)      
    except:
        return render_template('error3.html')
        pass     

@app.route('/download3', methods=["POST","GET"])
def download3():
    url = request.form["url"]
    print("Someone just tried to download", url)
    try: 
        with youtube_dl.YoutubeDL() as ydl:
          url = ydl.extract_info(url, download=False)
          print(url) #it will print all streams once
          video_streams = []
        for i in url['formats']:
            
            print(i['url'])  #it will print url of each stream 
            resolution = 'Audio'
            if i['height'] is not None:
                resolution = f"{i['height']}x{i['width']}"
                print(resolution) #it will print resolution of each stream
            video_streams.append({
                'resolution': resolution,
                'extension': i['ext'],
                'url': i['url']
            })
        print(type(video_streams))    
        video_streams = video_streams[::-1]
        
        context = {
            
            'title': url['title'], 'streams': video_streams,
            'description': url['description'], 'likes': url['like_count'],
            'thumb': url['thumbnail']
            
        }
        print(context['likes'])
        print(context['thumb'])
        try:
            download_link = url["entries"][-1]["formats"][-1]["url"]
        except:
            download_link = url["formats"][-1]["url"]
        print(download_link)
        return render_template('twitterpage.html', context=context , streams = video_streams)   
    except:
        return render_template('error2.html')
        pass
        


          
if __name__ == '__main__':
    app.run(port=80, debug=True)    