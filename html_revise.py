import os
import shutil 
import glob

book_title = "direct-knowledge"
book_name = "Direct Knowledge"

site_dir = '/Users/davidsmith/Documents/Sites/directknowledge.com/_book/'
os.chdir(site_dir)

## add the html (image, link, book info) above the toc on all pages. 
toc = '<nav id="TOC" role="doc-toc" class="toc-active">'
image_toc = toc
image_toc += '<a href="https://directknowledge.com/">'
image_toc += '<picture>' 
image_toc += '<source type="image/webp" srcset="/assets/direct-knowledge-cover-small.webp">'
image_toc += '<source type="image/webp" srcset="/assets/direct-knowledge-cover-small.png">'
image_toc += '<img class="shadow border" style="margin-bottom:12px;" width="192" height="288" src="/assets/direct-knowledge-cover-small.png" alt="Direct Knowledge Book Cover">'
image_toc += '</picture>' 
image_toc += '</a>' 


## find all js on page
js_1 = '<script src="site_libs/quarto-nav/quarto-nav.js"></script>'
js = js_1 + '\n'
js_2 = '<script src="site_libs/quarto-nav/headroom.min.js"></script>'
js = js + js_2 + '\n'
js_3 = '<script src="site_libs/clipboard/clipboard.min.js"></script>'
js = js + js_3 + '\n'
js_4 = '<script src="site_libs/quarto-search/autocomplete.umd.js"></script>'
js = js + js_4 + '\n'
js_5 = '<script src="site_libs/quarto-search/fuse.min.js"></script>'
js = js + js_5 + '\n'
js_6 = '<script src="site_libs/quarto-search/quarto-search.js"></script>'
js = js + js_6 + '\n'
js_7 = '<script src="site_libs/quarto-html/quarto.js"></script>'
js = js + js_7 + '\n'
js_8 = '<script src="site_libs/quarto-html/popper.min.js"></script>'
js = js + js_8 + '\n'
js_9 = '<script src="site_libs/quarto-html/tippy.umd.min.js"></script>'
js = js + js_9 + '\n'
js_10 = '<script src="site_libs/quarto-html/anchor.min.js"></script>'
js = js + js_10 + '\n'
js_11 = '<script src="site_libs/bootstrap/bootstrap.min.js"></script>'
js = js + js_11 + '\n' 
js = js + '</body>' 


#list of all html files
html_files = glob.glob("*.html", recursive=True)
print(html_files)

for html_file in html_files:
    # read in file to new variable and do replacement
    with open(html_file) as f:
        newText = f.read()
        # navbar 
        newText = newText.replace('class="navbar-brand" href="/"', 'aria-label="Direct Knowledge" class="navbar-brand" href="https://directknowledge.com"')
        newText = newText.replace('-logo.svg" alt="Direct Knowledge Logo"', '-logo.svg" alt="Direct Knowledge Logo" width="28" height="24" ')
        # sidebar 
        newText = newText.replace(toc, image_toc)
        # removes
        remove_1 = '<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" type="text/javascript"></script>'
        newText = newText.replace(remove_1, '')            
        # move js
        newText = newText.replace(js_1,'')
        newText = newText.replace(js_2,'')
        newText = newText.replace(js_3,'')
        newText = newText.replace(js_4,'')
        newText = newText.replace(js_5,'')
        newText = newText.replace(js_6,'')
        newText = newText.replace(js_7,'')
        newText = newText.replace(js_8,'')
        newText = newText.replace(js_9,'')
        newText = newText.replace(js_10,'')
        newText = newText.replace(js_11,'')
        newText = newText.replace('</body>', js)

        # remove extra lines
        newText = os.linesep.join([s for s in newText.splitlines() if s])

    # write out text
    with open(html_file, "w") as f:
        f.write(newText)

print(len(html_files))


