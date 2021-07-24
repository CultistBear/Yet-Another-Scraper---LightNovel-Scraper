This is a guide on how to add your own custom source so it works with [LightNovel-Scraper](https://github.com/CultistBear/Yet-Another-Scraper---LightNovel-Scraper).

Start by importing your own source and adding your source to the __Sources__, __SourcesSearchFunction__, __SourcesChapterLinksFunction__, __SourcesDownloadFunction__

![Custom Variables](https://user-images.githubusercontent.com/79724656/126852796-9c296bfb-8ef4-49e0-ba7a-bbc92e913fb8.PNG)

As for how the __SourcesSearchFunction__, __SourcesChapterLinksFunction__, __SourcesDownloadFunction__ are supposed to receive inputs and give outputs is discussed in depth below.

Also import __NovelLinks__, __NovelTitles__, __ChapterLinks__ in your script from __main__. it is recommended to use `from __main__ import NovelLinks,NovelTitles,ChapterLinks` due to import being cyclic/circular
<dl>
  <dt>SourcesSearchFunction</dt>
  <dd>
    
  The __SourcesSearchFunction__ recieves the Light Novel name (Input by the user beforehand) as an argument.

  ![How Function Receives the Data](https://user-images.githubusercontent.com/79724656/126853324-a13910dd-9757-4444-97fa-81a789b915d6.PNG)

  The <strong>SourcesSearchFunction</strong> has to search the source using the string provided by the user and append the search results i.e <i>novel title</i> and <i>novel links</i> in  <strong>NovelTitles</strong>, <strong>NovelLinks</strong> lists respectively.
  Note that the <i>novel title</i> and <i>novel links</i> indexes should match in the list.

  ![Append Novel Link and Title](https://user-images.githubusercontent.com/79724656/126853570-a51e4744-1705-4abe-8d7f-48761a3232cc.PNG)

  Which would then be used by the main script to ask the user which Light Novel to download.
  </dd>
</dl>

<dl>
  <dt>SourcesChapterLinksFunction</dt>
  <dd>
  The <strong>SourcesChapterLinksFunction</strong> recieves the index of Light Novel user wishes to download as per the <strong>NovelTitles</strong> list index.    

   ![Index Choosing](https://user-images.githubusercontent.com/79724656/126853705-96773ed6-402a-4e6f-9493-10f4f4f33f94.PNG)
   ![Chapter Range Function Input](https://user-images.githubusercontent.com/79724656/126853708-7a48c9c8-3f8a-4cfd-be84-57ad395d0483.PNG)

  The <strong>SourcesChapterLinksFunction</strong> has to then, at the end, append all the <i>chapter links</i> in the <strong>ChapterLinks</strong> list.

   ![Chapter Links Saving](https://user-images.githubusercontent.com/79724656/126854184-c0b88ade-ca07-4bc8-9006-4ca32963e294.PNG)
  
  This list would then be later used by the main script to inform the user how many total chapters there are and download the light novel by using the individual links stored in the <strong>ChapterLinks</strong> list.
  </dd>
  
<dl>
    <dt>SourcesDownloadFunction</dt>
    <dd>
  The <strong>SourcesDownloadFunction</strong> recieves the individual <i>chapter link</i> of the user selected range using the <strong>ChapterLinks</strong> list and the <strong>location</strong> to save the Light Novels to.
      

   ![SourcesDownloadFunction Input](https://user-images.githubusercontent.com/79724656/126854679-a22fd3d8-dd34-422c-8eb2-2c822b0d421a.PNG)
   ![Chapter Saving](https://user-images.githubusercontent.com/79724656/126854612-13f549d9-c8a2-4da6-9c75-8a9dc80359ec.PNG)

  The script also has to title the saved files.
    </dd>
</dl>

It is also highly recommended to have a good look at both [main](../main/main.py) and the [ReadLightNovelorg](../main/ReadLightNovelorg.py) python files to get a good idea on how everything works.

Lastly, New Sources are always welcome, feel free to share your custom sources with the community if you wish to do so.
  
Good Luck!
