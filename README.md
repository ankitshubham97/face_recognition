# piksep

Do you have a huge pile of photos of you and your friends and wish there existed some spell which would organize them according to who is there in the photos? Then piksep is what you are looking for! Just train it by feeding it some sample photos of your friends (so that piksep can learn how each of the persons look like!) before giving it the pile of unorganized photos.



## Installation

### Requirements

  * Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)

### Installation Options:

#### Installing on Mac:

You will be needing a few libraries in order to run piksep. Install these libraries. Skip if you already have them. We will be using `brew` and `pip` to install them.

Install cmake using:
```bash
brew install cmake
```

Install boost using:
```bash
brew install boost
brew install boost-python --with-python3
```

Install numpy using:
```bash
pip install numpy
```

Install dlib using:
```bash
pip install dlib
```

Install click using:
```bash
pip install click
```

Install Pillow using:
```bash
pip install Pillow
```

