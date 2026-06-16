from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_report(
    filename,
    plant,
    disease,
    confidence,
    cause,
    treatment,
    prevention,
    prediction_time
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("Plant Health Report", styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(f"<b>Plant:</b> {plant}", styles["BodyText"])
    )

    content.append(
        Paragraph(f"<b>Disease:</b> {disease}", styles["BodyText"])
    )

    content.append(
        Paragraph(
            f"<b>Confidence:</b> {confidence:.2f}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Prediction Time:</b> {prediction_time}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(f"<b>Cause:</b> {cause}", styles["BodyText"])
    )

    content.append(
        Paragraph(
            f"<b>Treatment:</b> {treatment}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Prevention:</b> {prevention}",
            styles["BodyText"]
        )
    )

    doc.build(content)