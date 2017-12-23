# -*- coding: utf-8 -*-

import os
import re
import webbrowser

# 构建并显示电影网站

# Styles and scripting for the page
__main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerSrc = $(this).attr('data-trailer_src')
            var sourceUrl = trailerSrc + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
__main_page_content = '''
    <!DOCTYPE html>
    <html lang="en">
      <body>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
          <div class="modal-dialog">
            <div class="modal-content">
              <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
              </a>
              <div class="scale-media" id="trailer-video-container">
              </div>
            </div>
          </div>
        </div>
    
        <!-- Main Page Content -->
        <div class="container">
          <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
              <div class="navbar-header">
                <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
              </div>
            </div>
          </div>
        </div>
        <div class="container">
          {movie_tiles}
        </div>
      </body>
    </html>
    '''

# A single movie entry html template
__movie_tile_content = '''
    <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer_src="{trailer_src}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" width="220" height="342">
        <h2>{movie_title}</h2>
    </div>
    '''


# 根据电影信息，构建可视化html内容
def __create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youku or youtube ID from the url
        trailer_url = movie.trailer_url
        youku_id_match = re.search(r'(id_)(\w+=*)(\.html)', trailer_url)
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', trailer_url)
        trailer_youku_id = youku_id_match.group(2) if youku_id_match else None
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        if trailer_youku_id is not None:
            trailer_src = 'http://player.youku.com/embed/' + trailer_youku_id
        else:
            trailer_src = 'http://youtube.com/embed/' + trailer_youtube_id

        # Append the tile for the movie with its content filled in
        content += __movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_src=trailer_src
        )
    return content


# 1.加载电影数据
# 2.将最终呈现的内容保存至本地文件fresh_tomatoes.html
# 3.通过浏览器访问本地文件fresh_tomatoes.html
def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = __main_page_content.format(movie_tiles=__create_movie_tiles_content(movies))

    # Output the file
    output_file.write(__main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
