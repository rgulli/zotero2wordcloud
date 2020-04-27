# zotero2wordcloud
Create a word cloud based on a specified field of a collection of papers from Zotero. 

## Installation instructions
1. Open a terminal window, and create a new virtual environment called `zotero2wordcloud`
  * Using [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html): `conda create --name zotero2wordcloud`
  * Using python: `python3.7 -m venv my_env`
2. Activate the new environment
  * `conda activate zotero2wordcloud` or `source zotero2wordcloud/bin/activate`
  * Note always work in this virtual environment when working on this project, and deactivate the environment when you're done. 
3. Navigate to the folder where you'd like to install this package
  * `cd <yourpath/GitHub/`
  * `mkdir zotero2wordcloud`
  * `cd zotero2wordcloud`
4. Install
* Using pip: `pip install zotero2wordcloud`
* Using Anaconda: `conda config --add channels conda-forge && conda install zotero2wordcloud`
  
## Usage instructions:
Before starting, you'll need three pieces of information from Zotery: library ID, library type, and API key. 

* Your personal library ID is available [from Zotero](https://www.zotero.org/settings/keys). 
* If you're using a group library, the ID is on the group's page `https://www.zotero.org/groups/yourgroupname`. Hover over the `Group Settings` link. 
* You will likely need to [create a new API key](https://www.zotero.org/settings/keys/new)
* If you're having trouble getting access to your Zotero library, check out example #1 in the `/examples` folder. Also see [Pyzotero documentation](https://pyzotero.readthedocs.io/en/latest/) for more information.

### Using terminal:
* `from zotero2wordcloud.zoterto2wordcloud import zotero2wordcloud`

### Using Anaconda
* `jupyter lab zotero2wordcloud.ipynb`

## Reporting issues
If you encounter an error while using this package, please open an issue on its [Github issues page](https://github.com/rgulli/zotero2wordcloud/issues).

## License
zotero2wordcloud is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). 
