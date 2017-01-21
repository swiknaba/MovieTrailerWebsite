import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
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
        <!-- the visible class does not solve the "display: none;" problem  -->
        <!--   see ReadMe for further information -->
        .visible{
            display: inline !important;
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
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.series').each(function(index, el) {
            console.log(el);
            $(el).children('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });
})
    </script>
    <script type="text/javascript" charset="utf-8">
    //yet another try to resolve the problem of the "display: none" problem
        var delay = 500;
        setTimeout(function(){
           $('#visible_error').load(function(){
               document.getElementById('visible_error').style.display = 'block';
           });
        }, delay);
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
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
            <a class="navbar-brand" href="fresh_tomatoes.html">Luds favourite movies</a>
            <a class="navbar-brand" href="fresh_tomatoes_series.html"> Luds favourite series</a>
          </div>
        </div>
      </div>
    </div>
    {movie_tiles}
  </body>
</html>
'''

# Header of one series containing several seasons
movie_tile_content_head = '''
<div class="container series">
    <h2>{series_title}</h2>
    <p>{series_description}</p>
'''

# A single seasons entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center visible" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" id="visible_error">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <p>{movie_description}</p>
    <p><strong>Duration: {movie_duration} min.</strong></p>
    </div>
'''

# Footer of one series containing several seasons
movie_tile_content_foot = '''
    <!-- <br><hr><br> -->
</div>
<br><br>
'''

def create_movie_tiles_content(series, seasons):
    """This method will put together HTML code that displays all series

    Input:
        series -- an arry containing all series as objects of class Series
        seasons -- an array containing one array per series, which again
                   contains all seasons als objects of class Movie
    Output:
        content -- HTML Code
    """
    content = ''
    for serie in range(0,len(series)):
        # Append the tile for the serie with its content filled in in 3 steps
        # 1. add the series titel, description
        content += movie_tile_content_head.format(
            series_title=series[serie].title,
            series_description=series[serie].storyline,
        )

        # 2. add all the seasons for the series
        for season in range(0,series[serie].count_seasons):
            # first extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', seasons[serie][season].trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', seasons[serie][season].trailer_youtube_url)
            trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                                  else None)
            # now append season
            content += movie_tile_content.format(
                movie_title=seasons[serie][season].title,
                poster_image_url=seasons[serie][season].poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                movie_description=seasons[serie][season].storyline,
                movie_duration=seasons[serie][season].duration
            )

        # 3. add a footer for seperation
        content += movie_tile_content_foot

    return content


def open_movies_page(series, seasons):
    """This method generates an HTML file

    Input:
        movies -- an arry containing all movies as objects of class Movie
    Output:
        fresh_tomatoes.html -- the HTML file representing the projects page
    """
    output_file = open('fresh_tomatoes_series.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(series, seasons))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()