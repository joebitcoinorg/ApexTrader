const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    canvas.width = 400;
    canvas.height = 400;

    // Game logic and rendering will go here

    function gameLoop() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      // Render the snake
      // Update the snake position
      requestAnimationFrame(gameLoop);
    }

    gameLoop();
