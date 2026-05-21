using UnityEngine;

public class DMg : MonoBehaviour
{

    private void OnTriggerStay2D(Collider2D collision)
    {
        if(collision.CompareTag("Player"))
        {
            Player1.instance.TakeDamage(-1);
        }
    }
}
