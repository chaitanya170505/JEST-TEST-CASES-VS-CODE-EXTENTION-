const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

function activate(context) {

  let disposable = vscode.commands.registerCommand(
    'ai-test-generator.generateTests',
    async function () {

      const editor = vscode.window.activeTextEditor;

      if (!editor) {
        vscode.window.showErrorMessage("No file open");
        return;
      }

      const code = editor.document.getText();

      vscode.window.showInformationMessage("Generating tests...");

      try {
        const response = await fetch('http://localhost:8000/generate-tests', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ code })
        });

        const data = await response.json();

        const testContent = data.result;

        const sourcePath = editor.document.fileName;
        const dir = path.dirname(sourcePath);
        const base = path.basename(sourcePath, path.extname(sourcePath));

        const testFilePath = path.join(dir, `${base}.test.js`);

        fs.writeFileSync(testFilePath, testContent);

        vscode.window.showInformationMessage("AI Tests Generated!");

      } catch (err) {
        console.error("FULL ERROR:", err);
        vscode.window.showErrorMessage(err.message || String(err));
      }
    }
  );

  context.subscriptions.push(disposable);
}

module.exports = { activate };