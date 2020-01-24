Flower Shop ⚘
=================

A audit history service

Usage
-----

With docker:
```
docker build .
docker run -v <absolute_path_to_sample_file>:/code/file <image_id>
```
Example:
```
docker run -v /Users/pc/Downloads/code-challange/sample.txt:/code/file a13cd2878b82
```
Output
```
⚘.⚘.⚘______Flower store_____⚘.⚘.⚘
For the bouquet design: AL10a15b5c30 - was generated a bouquet: AL10a15b5c
For the bouquet design: AS10a10b25 - was generated a bouquet: AS10a10b5a
For the bouquet design: BL15b1c21 - was generated a bouquet: BL15b1c5c
For the bouquet design: BS10b5c16 - was generated a bouquet: BS10b5c1c
For the bouquet design: CL20a15c45 - was generated a bouquet: CL20a15c10a
For the bouquet design: DL20b28 - was generated a bouquet: DL20b8b
```
_______
bash:
```
python generate_bouquet.py <absolute_path_to_sample_file> 
or
python generate_bouquet.py
```
Example:
```
python generate_bouquet.py /Users/pc/Downloads/code-challange/sample.txt
```
Output
```
⚘.⚘.⚘______Flower store_____⚘.⚘.⚘
For the bouquet design: AL10a15b5c30 - was generated a bouquet: AL10a15b5c
For the bouquet design: AS10a10b25 - was generated a bouquet: AS10a10b5a
For the bouquet design: BL15b1c21 - was generated a bouquet: BL15b1c5c
For the bouquet design: BS10b5c16 - was generated a bouquet: BS10b5c1c
For the bouquet design: CL20a15c45 - was generated a bouquet: CL20a15c10a
For the bouquet design: DL20b28 - was generated a bouquet: DL20b8b
```
