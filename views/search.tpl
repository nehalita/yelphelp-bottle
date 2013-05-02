%if 'error' in errors:
<b>{{errors['error']}} </b>
  <br>
  <br>
%end
<form action="search" method="POST">

    Please input your search term:
    <input type="text" name="search_term"> <br>
    Please input your location (address, city, zip code, or neighborhood):
    <br>
    Lattitude: 
    <input type="text" name="lat"> <br>
    Longitude: 
    <input type="text" name="long"> <br>
    <br>
  <input type="submit" value="search">
</form>
<br>
<br>
<a href="/main">Go back to the main page</a>
