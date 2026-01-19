# Profile Photo Instructions

To add your profile photo to your portfolio:

1. **Add your photo**: Place your profile image in this directory as `profile.jpg` (or another format like .png)
   - Recommended size: 400x400 pixels or larger (square format works best)
   - File size: Keep under 500KB for better performance
   - Supported formats: JPG, PNG, WebP

2. **Update the HTML**: The base.html template already references this image at:
   ```
   {{ url_for('static', filename='images/profile.jpg') }}
   ```

3. **Alternative formats**: If you use a different filename or format (e.g., profile.png), update the `src` attribute in [templates/base.html](../templates/base.html#L35) to match.

The profile photo will:
- Display as a circular image (150x150px on desktop, 120x120px on mobile)
- Have a white border with shadow effect
- Scale up slightly on hover for interactivity
- Be responsive across all device sizes

## Quick Setup
Simply add your image file as `static/images/profile.jpg` and the portfolio will automatically display it!
