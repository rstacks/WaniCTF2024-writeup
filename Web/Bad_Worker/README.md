# Bad_Worker

## Description

We created a web application that works offline.

https://web-bad-worker-lz56g6.wanictf.org

## Solution

- The "Fetch data" page of the provided website seemed significant. Clicking the "Fetch FLAG.txt" button on that page
caused "FLAG{This is not the flag!!}" to be displayed on the page. Nothing of note appeared in the
website's source, so I turned to [Burp Suite](https://portswigger.net/burp).
- I intercepted the request after pressing the "Fetch FLAG.txt" button. This was a GET request to
<code>/DUMMY.txt</code>. I changed it to instead fetch <code>/FLAG.txt</code>. After forwarding the edited request, the webpage
displayed the actual flag.

## Flag

FLAG{pr0gr3ssiv3_w3b_4pp_1s_us3fu1}
