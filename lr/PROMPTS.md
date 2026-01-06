# Custom Prompt Examples

This document provides example prompts for different photography scenarios. You can use these as templates to create custom prompts that better match your specific needs.

## Table of Contents

- [Understanding Custom Prompts](#understanding-custom-prompts)
- [Wedding Photography](#wedding-photography)
- [Product Photography](#product-photography)
- [Nature & Wildlife Photography](#nature--wildlife-photography)
- [Portrait Photography](#portrait-photography)
- [Event Photography](#event-photography)
- [Real Estate & Architecture](#real-estate--architecture)
- [Sports Photography](#sports-photography)
- [Stock Photography](#stock-photography)
- [Tips for Writing Effective Prompts](#tips-for-writing-effective-prompts)

## Understanding Custom Prompts

The AI uses your prompt to understand what metadata fields to generate and how to format them. A good prompt should:

1. **Specify required fields**: title, caption, headline, keywords, instructions, location
2. **Define format requirements**: JSON structure expected by the plugin
3. **Provide context**: Explain the type of photography and intended use
4. **Set tone and style**: Professional, creative, technical, etc.

**Important JSON Format Requirements:**
- Use `"keywords": "keyword1, keyword2, keyword3"` (comma-separated string)
- For hierarchical keywords, use `' > '` separator: `"keywords": "Nature > Wildlife > Birds, Sports > Team Sports"`
- Do NOT use JSON arrays for keywords: `["keyword1", "keyword2"]` ❌

## Wedding Photography

```
You are analyzing wedding photography for professional wedding albums and client delivery.

Please analyze this wedding photograph and provide:
1. A romantic and descriptive title (3-5 words)
2. A heartfelt caption that captures the emotion and moment (1-2 sentences)
3. A detailed description suitable for wedding albums (2-3 sentences) that tells the story of the moment
4. Relevant keywords including: wedding type (ceremony, reception, getting ready, portraits), emotions, locations, and specific moments
5. Post-processing suggestions for wedding photography (e.g., soft lighting, warm tones, vignetting)
6. Venue or location name if identifiable

Focus on emotional storytelling, romantic language, and moments that matter to couples. Consider lighting, emotions, interactions between people, and special details like flowers, rings, or décor.

Please format your response as JSON:
{
  "title": "romantic title here",
  "caption": "heartfelt caption capturing the emotion",
  "headline": "detailed description telling the story",
  "keywords": "Wedding > Ceremony, Emotions > Love, Wedding > Bride and Groom, Location > Venue Name",
  "instructions": "post-processing suggestions for wedding style",
  "location": "venue name or location"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

## Product Photography

```
You are analyzing product photography for e-commerce and marketing purposes.

Please analyze this product photograph and provide:
1. A clear, descriptive product title (3-5 words)
2. A concise product caption highlighting key features (1-2 sentences)
3. A detailed product description suitable for marketing (2-3 sentences)
4. Relevant keywords including: product category, features, materials, colors, style, and use cases
5. Photography and editing notes (lighting, background, composition suggestions)
6. Studio or location information if relevant

Focus on clarity, accuracy, and marketability. Describe the product objectively, highlight features and benefits, and consider the commercial context.

Please format your response as JSON:
{
  "title": "clear product title",
  "caption": "feature-focused caption",
  "headline": "detailed marketing description",
  "keywords": "Product Type > Category, Features > Specific Feature, Materials > Material Type, Colors > Color Name",
  "instructions": "photography and editing suggestions for product presentation",
  "location": "studio or shooting location if applicable"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

## Nature & Wildlife Photography

```
You are analyzing nature and wildlife photography for conservation documentation and artistic portfolios.

Please analyze this nature photograph and provide:
1. A descriptive title identifying the subject (3-5 words)
2. A caption describing the scene and behavior (1-2 sentences)
3. A detailed description including species information, habitat, and ecological context (2-3 sentences)
4. Relevant keywords including: taxonomy (kingdom/class/species), habitat, behavior, conservation status, and photographic technique
5. Technical recommendations for nature photography editing
6. Specific location if identifiable (park, reserve, geographic region)

Focus on accurate species identification, ecological context, and conservation messaging. Consider animal behavior, habitat characteristics, and the story behind the capture.

Please format your response as JSON:
{
  "title": "species or subject identification",
  "caption": "scene and behavior description",
  "headline": "detailed ecological description",
  "keywords": "Nature > Wildlife > Birds > Species Name, Habitat > Forest Type, Behavior > Specific Behavior, Photography > Wildlife Photography > Telephoto",
  "instructions": "technical editing recommendations for nature photography",
  "location": "specific location, park, or geographic region"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

## Portrait Photography

```
You are analyzing portrait photography for professional portfolios and client galleries.

Please analyze this portrait photograph and provide:
1. A concise title describing the portrait style (3-5 words)
2. A caption describing the mood, expression, and visual elements (1-2 sentences)
3. A detailed description of the lighting, composition, and emotional impact (2-3 sentences)
4. Relevant keywords including: portrait type (headshot, environmental, editorial), mood, lighting style, and composition
5. Retouching and editing guidance for professional portraits
6. Studio or location setting if identifiable

Focus on the subject's expression, mood, lighting quality, and the emotional connection created. Consider composition, use of negative space, and the story conveyed through the portrait.

Please format your response as JSON:
{
  "title": "portrait style description",
  "caption": "mood and visual elements description",
  "headline": "detailed description of lighting and impact",
  "keywords": "Photography > Portrait Photography > Style Type, Lighting > Light Type, Mood > Emotion, Composition > Technique",
  "instructions": "retouching and editing guidance",
  "location": "studio or location setting"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

## Event Photography

```
You are analyzing event photography for corporate and social events.

Please analyze this event photograph and provide:
1. A descriptive title identifying the event type and moment (4-6 words)
2. A caption describing the activity and participants (1-2 sentences)
3. A detailed description suitable for event documentation (2-3 sentences)
4. Relevant keywords including: event type, activities, venue type, mood, and key moments
5. Editing suggestions for event photography (color correction, exposure, cropping)
6. Venue name or location if identifiable

Focus on capturing the energy, activities, and atmosphere of the event. Consider group dynamics, venue characteristics, and newsworthy moments.

Please format your response as JSON:
{
  "title": "event type and moment description",
  "caption": "activity and participants description",
  "headline": "detailed event documentation",
  "keywords": "Events > Event Type, Activities > Specific Activity, Venue > Venue Type, Mood > Atmosphere",
  "instructions": "editing suggestions for event photography",
  "location": "venue name or location"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

## Real Estate & Architecture

```
You are analyzing architectural and real estate photography for property listings and architectural documentation.

Please analyze this architectural photograph and provide:
1. A clear title describing the structure or space (3-5 words)
2. A caption highlighting key architectural features (1-2 sentences)
3. A detailed description of the design, materials, and spatial qualities (2-3 sentences)
4. Relevant keywords including: property type, architectural style, features, materials, and rooms
5. Post-processing recommendations for real estate photography (perspective correction, HDR, staging)
6. Property location or neighborhood if identifiable

Focus on architectural details, spatial relationships, lighting, and selling features. Consider composition, vertical line correction, and highlighting the property's best attributes.

Please format your response as JSON:
{
  "title": "structure or space description",
  "caption": "key architectural features",
  "headline": "detailed design and material description",
  "keywords": "Real Estate > Property Type, Architecture > Style, Features > Specific Feature, Materials > Material Type, Rooms > Room Name",
  "instructions": "post-processing recommendations for real estate",
  "location": "property location or neighborhood"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

## Sports Photography

```
You are analyzing sports photography for athletic documentation and media coverage.

Please analyze this sports photograph and provide:
1. A dynamic title capturing the action (3-5 words)
2. A caption describing the play, athletes, and moment (1-2 sentences)
3. A detailed description of the athletic action and competitive context (2-3 sentences)
4. Relevant keywords including: sport type, action, athletes, equipment, and competitive level
5. Editing recommendations for sports photography (motion blur, freeze action, contrast)
6. Venue or competition location if identifiable

Focus on peak action moments, athletic skill, and competitive drama. Consider timing, motion, and the decisive moment that tells the story.

Please format your response as JSON:
{
  "title": "dynamic action description",
  "caption": "play and moment description",
  "headline": "detailed athletic action and context",
  "keywords": "Sports > Sport Type > Specific Action, Athletes > Position, Equipment > Gear, Competition > Level",
  "instructions": "editing recommendations for sports photography",
  "location": "venue or competition location"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

## Stock Photography

```
You are analyzing stock photography for commercial licensing and broad market appeal.

Please analyze this photograph for stock photography purposes and provide:
1. A clear, searchable title using common terms (3-5 words)
2. A descriptive caption highlighting commercial uses (1-2 sentences)
3. A detailed description emphasizing versatility and concepts (2-3 sentences)
4. Comprehensive keywords including: subjects, concepts, emotions, compositions, colors, and commercial applications
5. Technical quality notes and potential editing improvements
6. Generic location description (urban, rural, indoor, outdoor) without specific places

Focus on commercial viability, broad appeal, and searchability. Use universal language, avoid specific brand names, and emphasize concepts over specific details.

Please format your response as JSON:
{
  "title": "searchable commercial title",
  "caption": "commercial uses description",
  "headline": "versatility and concept emphasis",
  "keywords": "Concepts > Concept Name, Business > Industry, Emotions > Feeling, People > Demographics, Objects > Item Type, Colors > Color Palette",
  "instructions": "technical quality and editing improvements",
  "location": "generic location type (urban, office, outdoor, etc.)"
}

IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array. Include 15-20 diverse keywords for maximum searchability.
```

## Tips for Writing Effective Prompts

### 1. Be Specific About Your Needs
- Clearly state the photography genre and intended use
- Define the tone and style you want (professional, creative, technical, romantic, etc.)
- Specify any special requirements or constraints

### 2. Include All Required Fields
Your prompt should request:
- `title`: Short, descriptive title
- `caption`: Brief 1-2 sentence description
- `headline`: Detailed 2-3 sentence description
- `keywords`: Relevant search terms and categories
- `instructions`: Editing or usage suggestions
- `location`: Geographic or venue information when applicable

### 3. Specify Keyword Format
**Critical:** Always include this reminder in your prompt:
```
IMPORTANT: The keywords field must be a comma-separated string with hierarchical keywords using ' > ' separators, not an array.
```

For hierarchical keywords, add specific instructions:
```
For hierarchical keywords:
- Start with broad categories (Nature, Sports, Architecture)
- Progress to specific subcategories
- End with detailed descriptors
- Use ' > ' to separate hierarchy levels
- Examples: "Nature > Wildlife > Birds > Eagles", "Sports > Team Sports > Football"
```

### 4. Provide Context Examples
Include examples in your prompt to guide the AI:
```
Example keywords format: "Wedding > Ceremony, Emotions > Love, Photography > Wedding Photography"
Example caption: "A romantic moment during the first dance, captured with soft golden hour lighting"
```

### 5. Test and Iterate
- Start with one of the templates above
- Test on several representative photos
- Adjust the prompt based on the results
- Fine-tune language and emphasis as needed

### 6. Consider Your Workflow
- For batch processing, use consistent prompts for similar photo types
- Create multiple custom prompts for different photography scenarios
- Save successful prompts as presets for reuse

### 7. Language Considerations
If you need responses in languages other than English, add this at the beginning of your prompt:
```
IMPORTANT: Please respond in [Language] language. All text fields (title, caption, headline, keywords, instructions, location) should be in [Language].
```

## Technical Notes

### JSON Format Requirements
The plugin expects responses in this exact JSON structure:
```json
{
  "title": "string",
  "caption": "string",
  "headline": "string",
  "keywords": "string with comma-separated values",
  "instructions": "string",
  "location": "string"
}
```

**Common mistakes to avoid:**
- ❌ Using JSON arrays for keywords: `"keywords": ["tag1", "tag2"]`
- ✅ Use comma-separated strings: `"keywords": "tag1, tag2"`
- ❌ Using different field names: `"description"` instead of `"headline"`
- ✅ Use exact field names specified above

### Working with Existing Keywords
The plugin automatically includes existing photo keywords as context in the AI prompt. The AI will:
- Reference existing keywords (like people names, project identifiers, events) in captions and descriptions
- Suggest complementary keywords that expand on the existing context
- Preserve the context provided by your manual keyword assignments

You don't need to explicitly request this in your custom prompt—it's handled automatically.

### Metadata Integration
When "Include GPS and EXIF Data" is enabled, the plugin automatically sends:
- GPS coordinates and location metadata
- Camera make, model, and lens information
- Shooting settings (aperture, shutter speed, ISO, focal length)
- Date and time captured
- Image dimensions

The AI will use this information to enhance its analysis. You can reference this in your prompt:
```
Consider the technical metadata provided (camera settings, GPS coordinates, capture time) when analyzing the photograph and generating keywords.
```

## Support and Feedback

If you create custom prompts that work particularly well for your photography needs, consider sharing them with the community! Report issues or share prompt examples at:
https://github.com/obelix74/docs/issues

For more information about the AI Image Tagger plugin, visit:
https://obelix74.github.io/docs/lr.html
