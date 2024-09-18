# tabbed_browser_links
A python program to look at all open Brave browser tabs and output the tabs' title and URLs into a double-spaced txt file.

Do you have a lot of tabs open in your browser windows taking up valuable system resources?

This python program "browser_link_dl.py" will put those URLs into a double-spaced txt file with titles/descriptors so you can look at them later!
I will also include an Apps Script for a Google Docs file so you can hyperlink the URLs if you upload your txt file to a Docs file: makelinksblue.txt

1. Preparation
   - We will need to start your browser with a new instance so closing all your browsers first. You can open your windowed 
    tabs with the same instance.

2. Enable Remote Debugging
   - Go to the browser's directory and run the following code in on the command line, powershell, or terminal of VS Code (what      I use).
   - Brave: brave.exe --remote-debugging-port=9222
   - Chrome: chrome.exe --remote-debugging-port=9222
   - If you're using macOS or Linux, you might need to replace chrome.exe with the correct path to your Chrome binary. For           example:
       - macOS: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
       - Linux: google-chrome --remote-debugging-port=9222

    If done correctly, a new instance of your browser will open. From here, you can visit your History and reopen all the windowed tabs.

   If there are any issues check that the DevTools API for your browser is running: http://localhost:9222/json
   If this shows a JSON response with information about open tabs, it means your broswer is running correctly with debugging.
   If it does not connect, close your browser and restart your computer and start at step 2.
    
4. Go to your IDE (VS Code)
   - Open up browser_link_dl.py or copy contents from Github to a new file and name accordingly.

5. Install Required Libraries
   - In your terminal install requests: pip install requests
  
6. Run the file
   - Running the file will create "brave_tabs.txt" in the same location as your python file.
   - Change the output txt file name in the python file's code if you want a different output file name.

There you have it! A list of your browser's tabs! Feel free to change the code to suit your needs!
