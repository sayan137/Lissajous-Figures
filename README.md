<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Oscillatory Motion with Phase and Frequency Variations</h1>
    <p>This project visualizes the combined oscillatory motion of two systems, each having different angular frequencies and a phase difference, using Python's Matplotlib and NumPy libraries. The animation provides an intuitive understanding of oscillatory dynamics and how phase relationships and frequencies affect motion.</p>

  <h2>Features</h2>
    <ul>
        <li><strong>Customizable Parameters:</strong>
            <ul>
                <li>Amplitude, phase difference, angular frequencies, and frame speed can be adjusted.</li>
            </ul>
        </li>
        <li><strong>Multiple Visual Representations:</strong>
            <ul>
                <li>Combined motion (Lissajous-like patterns) and individual motions in subplots.</li>
                <li>Real-time depiction of motion dynamics using arrows and grid guides.</li>
            </ul>
        </li>
        <li><strong>Mathematical Insights:</strong>
            <ul>
                <li>Displays equations and relationships between the parameters (e.g., angle, phase).</li>
            </ul>
        </li>
    </ul>

   <h2>Animation Overview</h2>
    <p>The animation comprises four subplots:</p>
    <ol>
        <li><strong>Bottom Right:</strong> Shows the resultant motion combining two oscillatory components. Visualized with arrows representing components and resultant vectors.</li>
        <li><strong>Top Left:</strong> Highlights the individual motion with perpendicular components. Displays circular motion arising from oscillation.</li>
        <li><strong>Top Right:</strong> Plots the x-component versus the y-component, forming patterns that evolve with time.</li>
        <li><strong>Bottom Left:</strong> Annotates the mathematical equations describing the motion and the phase angle.</li>
    </ol>

   <h2>How to Use</h2>
    <ol>
        <li><strong>Customizing Parameters:</strong> Update the values for <code>a</code>, <code>b_1</code>, <code>omega_a</code>, <code>omega_b</code>, <code>phase</code>, and <code>theta</code> as per the desired motion.</li>
        <li><strong>Running the Code:</strong> Execute the Python script to generate the animation.</li>
        <li><strong>Saving the Animation:</strong> Uncomment the line <code>#ani.save(...)</code> to save the animation as a GIF.</li>
    </ol>

   <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Matplotlib</li>
        <li>NumPy</li>
    </ul>

   <h2>Output Example</h2>
    <p>The animation showcases dynamic vector motion and evolving patterns, providing visual insights into oscillatory systems and phase interactions.
    </p>

  <h2>Acknowledgments</h2>
    <p>Inspiration for writing this code came from intereactions with my college professors and a book on acoustics by DP Roychowdhury .</p>
<h2>License</h2>
    <p>
        This project is licensed under the MIT License. Feel free to use, modify, and distribute this code with attribution.
</body>
</html>
