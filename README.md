# RealitySplit – Narrative Framing Intelligence

RealitySplit exposes narrative framing and emotional manipulation in media. Paste any news article to instantly see how the same facts are framed across five ideological lenses.

## Tech Stack
- **Frontend**: Next.js 15, TypeScript, Tailwind CSS v4, shadcn/ui, Framer Motion, Recharts
- **Backend**: FastAPI (Python 3.11), Gemini 2.0 Flash

## Getting Started

### Backend Setup
1. Navigate to `backend/`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your Gemini API Key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the server:
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`.

### Frontend Setup
1. Navigate to `frontend/`
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:3000`.

## Features
- **5 Ideological Lenses**: Conservative, Progressive, Corporate/Market, Activist, Global South.
- **Manipulation Analysis**: Structured scoreboard with emotional intensity, loaded language, and urgency metrics.
- **Bias Heatmap**: Visual representation of systemic bias levels.
- **Polarization Meter**: Real-time gauge of narrative divergence.
- **Interactive Highlighting**: View specific phrases that drive ideological framing.
# RealitySplit
