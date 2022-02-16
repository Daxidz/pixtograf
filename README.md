# Pix to Graf
Extract colors from a pixelart (or any image) and create files in black and white to feed a laser cut machine SW

# Example
Taken this input image:

![](test_img/test_extract.png)

and this command:

```bash
python3 pixtograf.py -i test_img/test_extract.png -o test_img/test_out -r 10
```

it produces:


![](test_img/test_out(135,31,33,255).png)
![](test_img/test_out(194,153,108,255).png)
![](test_img/test_out(68,56,67,255).png)
![](test_img/test_out(80,99,102,255).png)