# Format of training prompt
defaultPrompt = """I am a Cardiologist. My patient asked me what this means:

Input: Normal left ventricular size and systolic function. EF > 55 %. Normal right ventricular size and systolic function. Normal valve structure and function

Output: Normal pumping function of the left and right side of the heart. Heart valves are normal

-

Input: severely dilated left ventricle with severely reduced systolic function. EF 25 %. Mildly dilated right ventricle with moderately reduced systolic function. Dilated mitral annulus with moderate central mitral regurgitation. Dilated ascending aorta with moderate central aortic regurgitation. Prior report was reviewed and systolic function as well as mitral regurgitation appears worse

Output: Heart is enlarged with reduced pumping if the right as well as left side of the heart. Mitral valve is severely leaky. Large artery coming out of the heart (aorta) is enlarged. Aortic valve is moderately leaky. These findings are worse compared to an earlier study

-
Input: {}

Output:"""
