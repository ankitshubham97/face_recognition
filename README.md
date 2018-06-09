# Piksep

Are your photographs unorganised? Do they give you a hard time when you arrange? Then Piksep is what you're looking for. Piksep organises your photographs with the help of facial recognition. All you have to do is feed it some sample photos so it can learn the facial appearance before giving it the unorganized pile of the photographs.



## Installation

### Requirements

  * Python 2.7
  * macOS or Linux (Support for Windows coming soon!)

### Prerequisites:

#### Installing prerequisites on Mac:

You will be needing a few libraries in order to run Piksep. Install these libraries. Skip if you already have them. We will be using `brew` and `pip` to install them.

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

#### Installing prerequisites on Linux:

You need to make sure that the libraries listed in the above section are installed. Use `apt-get` for this.

<!--#### Installing prerequisites on Windows:

Download and install anaconda for windows from [https://www.anaconda.com/download/].

From the anaconda command prompt type the following commands:

```bash
conda install cmake
```

```bash
conda install boost
```

```bash
conda install numpy
```

```bash
conda install -c conda-forge dlib=19.4
```

```bash
conda install click
```

```bash
conda install pillow
```
-->
### Getting Piksep

Choose a folder where you want to keep Piksep. Either download the entire code from [https://github.com/ankitshubham97/piksep](https://github.com/ankitshubham97/piksep) as zip file and unzip it or use ```git clone https://github.com/ankitshubham97/piksep.git```

## Using Piksep

Open the root folder. You will see 2 folders: `input` and `unknown`.

![](https://github.com/ankitshubham97/piksep/blob/gifbranch/piksep_1.gif)
 
### Training photos

In the 'input' folder, you will put sample photos of all those people for whom you are going to run Piksep. To do this, make separate folders for all the persons and name those folders after the names of the corresponding persons.

![](https://github.com/ankitshubham97/piksep/blob/gifbranch/piksep_2a.gif)
 
I had already created 2 folders `lucky` and `happy` with sample photos in them. I just copy-pasted them in the `input` folder.

Put not more than 2 or 3 sample photos in each of them (better if they have varying expressions :) ).

![](https://github.com/ankitshubham97/piksep/blob/gifbranch/piksep_2b.gif)
 
Make sure that these photos do not have any other other faces too apart from the person intended (as you can see in the above GIF)

This is for training Piksep. It lets it learn what each of the persons look like.

### Unorganized photos

Put all the unorganized photos directly in the `unknown` folder. Note that all the photos must be 'directly' put in that folder, i.e. there should not be any folders in `unknown` folder.

![](https://github.com/ankitshubham97/piksep/blob/gifbranch/piksep_3.gif)

I pasted my unorganized photos into the `unknown` folder as shown in the above GIF.

### Running Piksep

Open a terminal in the root directory. Run Piksep using the command 
```bash
python run.py
```

![](https://github.com/ankitshubham97/piksep/blob/gifbranch/piksep_4.gif)
 
It should start executing. You will see messages on the terminal reporting you about the execution process.

### Getting the organized photos

In the end, you should see this message: `Find the folders in the 'output' folder.` It means that execution is over and you can find the organized pile at a newly created folder `output`.

![](https://github.com/ankitshubham97/piksep/blob/gifbranch/piksep_5.gif)

Open the `output` folder and you will see different folders by the name of people for which you trained Piksep for. You will find the photos of a particular person in the folder named after that person.

![](https://github.com/ankitshubham97/piksep/blob/gifbranch/piksep_6.gif)

## Caveats

* It is definitely not 100% accurate.
* It does not work that well for children
* It does not work well if the person is wearing sunglasses

## Special mention

This project is forked from Adam Geitgey's repository [face_recognition](https://github.com/ageitgey/face_recognition). Visit that repository for a deeper insight of face recognition mechanism!
