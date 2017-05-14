function main()
{
    "use strict";
    var url       = document.URL,
        greetings = document.getElementById('greetings');

    if (url &&
        (url = url.split('#')[1]))
    {
        url = decodeURI(url).split(',').join(',<br/>');
        greetings.innerHTML = 'Kedves<br/>' + url + '!';
    }
}
