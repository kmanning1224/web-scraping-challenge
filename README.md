<!DOCTYPE html>
<html lang="en">

<head>
  <title>Missions to Mars </title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet/text" href="style.css">
</head>
<body>

	<div class="row">
		<div class="col-md-12">
			<div class="jumbotron text-center" style="background-color:goldenrod;">
				<h1>
					Mission to Mars
				</h1>
				<p>
					<a class="btn btn-primary btn-lg" style="background-color:rgb(19, 19, 24);" href="/scrape" role="button">Mission to Scrape Mars</a>
				</p>
			</div>
			<div class="page-header">
				<div class="col-md-12 text-left">
                        
                              <h2 text-align="center"><b>Latest Mars News</b></h2>
                              <h4 class="heading">{{ mars_data.news_title }}</h4>
                              <p>{{ mars_data.news_info }}</p>
                            </div>
				</div>
            </div>
            <div class="container">
            <div class="row">
                <div class="col-sm-8 text-left">
                  <div class="page-header">
                    <h2>
                      Mars feautured image
                    </h2>
                  <p class="aligncenter">
                  <img class="align" src="{{ mars_data.featured_image}}" height="500" width="700" class="img-responsive">
                </p>
                </div>
              </div>
              <div class="container-fluid text-center">
                  <div class="row">
                    <div class="col-sm-4 text-center">
                      <div class="page-header">
                        <h2>
                          Mars Facts
                        </h2>
                        <p>
                      {{mars_data.mars_fact | safe}}</p>
                    </div>
                  </div>
                    <div class = "container">
                      <div class="col-sm-8 center">
                      <div class="page-header">
                        <h3>
                          Images of Mars Hemispheres
                        </h3>
                    <div id="myCarousel" class="carousel slide" data-ride="carousel" height="300" width="400">
                      <!-- Indicators -->
                      <ol class="carousel-indicators" height="300" width="400">
                        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                        <li data-target="#myCarousel" data-slide-to="1"></li>
                        <li data-target="#myCarousel" data-slide-to="2"></li>
                        <li data-target="#myCarousel" data-slide-to="3"></li>
                      </ol>
                    
                      <!-- Wrapper for slides -->
                      <div class="carousel-inner" role="listbox">
                        <div class="item active">
                          <img src="{{ mars_data.img_link_cerb}}">
                          <div class="carousel-caption">
                            <h3>{{mars_data.title_cerb}}</h3>
                          
                          </div>
                        </div>
                    
                        <div class="item">
                          <img src="{{ mars_data.img_link_schi}}">
                          <div class="carousel-caption">
                            <h3>{{mars_data.title_schi}}</h3>
                            
                          </div>
                        </div>
                    
                        <div class="item">
                          <img src="{{ mars_data.img_link_syr}}">
                          <div class="carousel-caption">
                            <h3>{{mars_data.title_syr}}</h3>
                          </div>
                        </div>
                    
                        <div class="item">
                          <img src="{{ mars_data.img_link_vall}}">
                          <div class="carousel-caption">
                            <h3>{{mars_data.title_vall}}</h3>
                        
                          </div>
                        </div>
                      </div>
                    
                      <!-- Left and right controls -->
                      <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>
                    </div>
                  </div>
                </div>
				</div>
			</div>
		</div>
	</div>
</div>
</body>
</html>
