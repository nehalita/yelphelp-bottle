%if 'error' in errors:
<b>{{errors['error']}} </b>
  <br>
  <br>
%end
<form action="search" method="POST">

    Type a restaurant you'd like to compare:
    <input type="text" name="search_term"> <br>
    Approximately where is this? (address, city, zip code, or neighborhood):
    <input type="text" name="location"> <br>
    <br>
  <input type="submit" value="search">
</form>
<br>
<br>
<a href="/main">Go back to the main page</a>
