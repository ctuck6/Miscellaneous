#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

struct PPM {
	int height = 0, width = 0, top = -1, bottom = -1, left = -1, right = -1;
	vector<vector<int>> pixels;
};

PPM createPPM(string, string, string);
void drawBox(PPM, string); // Draws box around foreground object
int distanceFormula(pair<int, int>, pair<int, int>, pair<int, int>);

int main(int argc, char const *argv[]) {
	string foreground = "foreground.ppm";
	string background = "background.ppm";
	string output = "output.ppm";

	PPM ppmObject = createPPM(background, foreground, output);
	drawBox(ppmObject, output);

	return 0;
}

PPM createPPM(string background, string foreground, string output) {
	string type;
	int height, width, maxIntensity;
	PPM ppmObject;

	ifstream backgroundPpm, foregroundPpm;

	backgroundPpm.open(background);
	foregroundPpm.open(foreground);
	backgroundPpm >> type; // Need to keep them at the same line
	foregroundPpm >> type; // Need to keep them at the same line
	backgroundPpm >> height >> width >> maxIntensity; // Need to keep them at the same line
	foregroundPpm >> height >> width >> maxIntensity; // Need to keep them at the same line
	ppmObject.height = height, ppmObject.width = width;

	for (int i = 0; i < (height * width); i++) {
		pair<int, int> red, green, blue; // Stores foreground and background red, green, and blue

		backgroundPpm >> red.first >> green.first >> blue.first;
		foregroundPpm >> red.second >> green.second >> blue.second;

		int difference = distanceFormula(red, green, blue); // Gets distance formula for both triplets

		if (difference >= 30) { // This means pixel is foreground candidate
			ppmObject.pixels.push_back({red.second, green.second, blue.second});

			if (ppmObject.top == -1) { // set upper most
				ppmObject.top = (i / width);
			}

			if ((i / width) > ppmObject.bottom) { // set lower most
				ppmObject.bottom = (i / width);
			}

			if (ppmObject.left == -1 or (i % height) < ppmObject.left) { // set left most
				ppmObject.left = (i % height);
			}

			if ((i % height) > ppmObject.right) { // set right most
				ppmObject.right = (i % height);
			}
		} else { // Make part of background
			ppmObject.pixels.push_back({255, 255, 255});
		}
	}

	backgroundPpm.close();
	foregroundPpm.close();

	return ppmObject;
}

void drawBox(PPM ppmObject, string output) {
	ofstream outputPpm;

	outputPpm.open(output);
	outputPpm << "P3\n";
	outputPpm << ppmObject.height << " " << ppmObject.width << "\n";
	outputPpm << "255\n";

	for (int i = 0; i < ppmObject.pixels.size(); i++) {
		if (i % 5 == 0) {
			outputPpm << "\n";
		}

		if ((i / ppmObject.width) == ppmObject.top and // top boundary
			(i % ppmObject.height) >= ppmObject.left and
			(i % ppmObject.height) <= ppmObject.right) {

			outputPpm << 255 << " " << 0 << " " << 0 << " "; // set red
		} else if ((i / ppmObject.width) == ppmObject.bottom and // bottom boundary
			(i % ppmObject.height) >= ppmObject.left and
			(i % ppmObject.height) <= ppmObject.right) {

			outputPpm << 255 << " " << 0 << " " << 0 << " ";
		} else if ((i % ppmObject.height) == ppmObject.left and // left boundary
			(i / ppmObject.width) >= ppmObject.top and
			(i / ppmObject.width) <= ppmObject.bottom) {

			outputPpm << 255 << " " << 0 << " " << 0 << " ";
		} else if ((i % ppmObject.height) == ppmObject.right and // right boundary
			(i / ppmObject.width) >= ppmObject.top and
			(i / ppmObject.width) <= ppmObject.bottom) {

			outputPpm << 255 << " " << 0 << " " << 0 << " ";
		} else {
			outputPpm << ppmObject.pixels[i][0] << " " << ppmObject.pixels[i][1] << " " << ppmObject.pixels[i][2] << " ";
		}
	}

	outputPpm.close();
}

int distanceFormula(pair<int, int> red, pair<int, int> green, pair<int, int> blue) {
	return sqrt(
		pow(red.first - red.second, 2) +
		pow(green.first - green.second, 2) +
		pow(blue.first - blue.second, 2)
	);
}
