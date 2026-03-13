# Images Guide

This guide explains the images used on the site and how to replace them with your own.

## Current Image Sources

The site currently uses placeholder images from Unsplash. These are high-quality, professional images that work well for the security/protection theme.

### Hero Section Background
- **Current**: Private jet/airplane image
- **Location**: `static/css/styles.css` - `.hero-background`
- **Replace**: Update the `background-image` URL in CSS or add your own image to `static/images/hero-bg.jpg`

### Why Choose Us Section
- **Current**: Security operations center image
- **Location**: `templates/index.html` - Why Choose Us section
- **Image URL**: `https://images.unsplash.com/photo-1550751827-4bd374c3f58b`
- **Replace**: Add your image to `static/images/security-ops.jpg` and update the template

### Process Section
- **Current**: Professional team coordination image
- **Location**: `templates/index.html` - Process section
- **Image URL**: `https://images.unsplash.com/photo-1451187580459-43490279c0fa`
- **Replace**: Add your image to `static/images/team-coordination.jpg` and update the template

## Adding Your Own Images

### Step 1: Add Images to Project
1. Place your images in the `static/images/` directory
2. Recommended formats: JPG, PNG, WebP
3. Recommended sizes:
   - Hero background: 1920x1080px (or larger)
   - Section images: 800x600px minimum

### Step 2: Update Templates

**For Hero Background** (`static/css/styles.css`):
```css
.hero-background {
    background-image: url('/static/images/hero-bg.jpg');
}
```

**For Section Images** (`templates/index.html`):
```html
<img src="{{ url_for('static', filename='images/your-image.jpg') }}" alt="Description" class="section-image">
```

## Image Recommendations

### Hero Section
- Private jet/airplane
- Professional security team
- Executive protection scene
- Modern security operations

### Why Choose Us Section
- Security operations center
- Professional security personnel
- Advanced technology/monitoring
- Command center

### Process Section
- Team coordination
- Professional consultation
- Security planning
- Technology integration

## Free Image Resources

- **Unsplash**: https://unsplash.com (free, high-quality)
- **Pexels**: https://pexels.com (free stock photos)
- **Pixabay**: https://pixabay.com (free images)

Search terms: "security", "protection", "executive protection", "bodyguard", "surveillance"

## Image Optimization Tips

1. **Compress images** before uploading (use TinyPNG or similar)
2. **Use WebP format** for better compression (with JPG fallback)
3. **Optimize file sizes** - aim for < 500KB per image
4. **Use appropriate dimensions** - don't upload 4K images if displaying at 800px

## Current Image URLs (for reference)

- Hero: `https://images.unsplash.com/photo-1556388158-158ea5ccacbd`
- Why Choose Us: `https://images.unsplash.com/photo-1550751827-4bd374c3f58b`
- Process: `https://images.unsplash.com/photo-1451187580459-43490279c0fa`

All images are set to load with appropriate dimensions and quality settings.
